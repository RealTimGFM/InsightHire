from pathlib import Path

from flask import Flask, abort, flash, g, redirect, render_template, request, session, url_for

from data.companies import COMPANIES, COMPANY_LIST
from data.demo_resume import DEMO_RESUME
from data.pricing import BUSINESS_MODEL_NOTES, FEATURE_COMPARISON, INSTITUTION_PARTNERSHIP_POINTS, PRICING_PLANS
from data.site_content import (
    AI_PANEL,
    COMPANY_MARQUEE,
    FEATURE_HIGHLIGHTS,
    HOW_IT_WORKS,
    LANDING_SNAPSHOT_STATS,
    ROADMAP_ITEMS,
    VALUE_PILLARS,
    VERIFIED_DASHBOARD_CONTENT,
    VERIFIED_PREVIEW_CARDS,
)
from utils.auth import (
    authenticate_user,
    create_user,
    get_user_by_email,
    get_user_by_id,
    init_db,
    login_required,
    login_user,
    logout_user,
    role_required,
    seed_demo_users,
)
from utils.helpers import get_dashboard_recommendations, get_quick_stats, get_recent_activity, search_companies


BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / "instance"
DATABASE_PATH = INSTANCE_DIR / "users.db"

app = Flask(__name__, instance_path=str(INSTANCE_DIR), instance_relative_config=True)
app.config.update(
    SECRET_KEY="insight-hire-preview-secret-key",
    DATABASE=str(DATABASE_PATH),
)

INSTANCE_DIR.mkdir(parents=True, exist_ok=True)
init_db(app.config["DATABASE"])
seed_demo_users(app.config["DATABASE"])


@app.before_request
def load_current_user():
    user_id = session.get("user_id")
    g.user = get_user_by_id(app.config["DATABASE"], user_id) if user_id else None


@app.context_processor
def inject_global_template_values():
    return {
        "current_user": g.get("user"),
        "current_year": 2026,
        "app_name": "INSIGHT HIRE",
    }


def validate_credentials(email, password):
    errors = []

    if not email or "@" not in email or "." not in email:
        errors.append("Enter a valid email address.")
    if not password or len(password) < 6:
        errors.append("Password must be at least 6 characters long.")

    return errors


@app.route("/")
def landing():
    if g.user:
        return redirect(url_for("dashboard"))

    featured_companies = COMPANY_LIST
    pricing_preview = PRICING_PLANS[:2]

    return render_template(
        "landing.html",
        featured_companies=featured_companies,
        feature_highlights=FEATURE_HIGHLIGHTS,
        value_pillars=VALUE_PILLARS,
        how_it_works=HOW_IT_WORKS,
        company_marquee=COMPANY_MARQUEE,
        landing_snapshot_stats=LANDING_SNAPSHOT_STATS,
        pricing_preview=pricing_preview,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if g.user:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        errors = validate_credentials(email, password)
        if errors:
            for error in errors:
                flash(error, "warning")
            return render_template("login.html", email=email)

        user = authenticate_user(app.config["DATABASE"], email, password)
        if not user:
            flash("We could not match that email and password.", "danger")
            return render_template("login.html", email=email)

        login_user(user)
        flash("Welcome back to INSIGHT HIRE.", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if g.user:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        errors = validate_credentials(email, password)
        if get_user_by_email(app.config["DATABASE"], email):
            errors.append("An account with that email already exists.")

        if errors:
            for error in errors:
                flash(error, "warning")
            return render_template("signup.html", email=email)

        user = create_user(app.config["DATABASE"], email, password)
        login_user(user)
        flash("Your account is ready. Explore the dashboard to start researching companies.", "success")
        return redirect(url_for("dashboard"))

    return render_template("signup.html")


@app.route("/demo-login", methods=["POST"])
def demo_login():
    user = get_user_by_email(app.config["DATABASE"], "demo@insighthire.com")
    if not user:
        flash("Preview access is temporarily unavailable.", "danger")
        return redirect(url_for("landing"))

    login_user(user)
    flash("Preview access enabled. Welcome to INSIGHT HIRE.", "success")
    return redirect(url_for("dashboard"))


@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("landing"))


@app.route("/dashboard")
@login_required
def dashboard():
    if g.user["role"] == "verified_employee":
        return redirect(url_for("verified_dashboard"))

    return render_template(
        "dashboard.html",
        recommendations=get_dashboard_recommendations(),
        quick_stats=get_quick_stats(),
        recent_activity=get_recent_activity(),
        ai_panel=AI_PANEL,
        demo_resume=DEMO_RESUME,
    )


@app.route("/verified-dashboard")
@role_required("verified_employee")
def verified_dashboard():
    return render_template(
        "verified_dashboard.html",
        content=VERIFIED_DASHBOARD_CONTENT,
        preview_cards=VERIFIED_PREVIEW_CARDS,
    )


@app.route("/verified-preview")
@role_required("verified_employee")
def verified_preview():
    return render_template("preview_verified.html", preview_cards=VERIFIED_PREVIEW_CARDS)


@app.route("/search")
@login_required
def search():
    query = request.args.get("q", "").strip()
    results = search_companies(query)

    return render_template(
        "search.html",
        query=query,
        results=results,
        total_results=len(results),
    )


@app.route("/companies/<slug>")
@login_required
def company_detail(slug):
    company = COMPANIES.get(slug)
    if not company:
        abort(404)

    return render_template(
        "company_detail.html",
        company=company,
        demo_resume=DEMO_RESUME,
    )


@app.route("/pricing")
def pricing():
    return render_template(
        "pricing.html",
        plans=PRICING_PLANS,
        comparison_rows=FEATURE_COMPARISON,
        business_model_notes=BUSINESS_MODEL_NOTES,
        institution_partnership_points=INSTITUTION_PARTNERSHIP_POINTS,
    )


@app.route("/roadmap")
def roadmap():
    return render_template("roadmap.html", roadmap_items=ROADMAP_ITEMS)


@app.errorhandler(404)
def page_not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
