const toastRoot = document.getElementById("toast-root");
const modal = document.getElementById("demo-modal");
const modalTitle = document.getElementById("modal-title");
const modalMessage = document.getElementById("modal-message");
const modalClose = document.getElementById("modal-close");

function showToast(message, detail = "") {
    if (!toastRoot || !message) {
        return;
    }

    const toast = document.createElement("div");
    toast.className = "toast";
    toast.innerHTML = `
        <div class="toast-title">${message}</div>
        ${detail ? `<div class="toast-detail">${detail}</div>` : ""}
    `;

    toastRoot.appendChild(toast);

    window.setTimeout(() => {
        toast.style.opacity = "0";
        toast.style.transform = "translateY(8px)";
        window.setTimeout(() => toast.remove(), 220);
    }, 4200);
}

function openModal(title, message) {
    if (!modal || !modalTitle || !modalMessage) {
        return;
    }

    modalTitle.textContent = title || "INSIGHT HIRE";
    modalMessage.textContent = message || "";
    modal.classList.remove("hidden");
    modal.setAttribute("aria-hidden", "false");
}

function closeModal() {
    if (!modal) {
        return;
    }

    modal.classList.add("hidden");
    modal.setAttribute("aria-hidden", "true");
}

document.querySelectorAll("[data-toast-message]").forEach((button) => {
    button.addEventListener("click", () => {
        showToast(button.dataset.toastMessage, button.dataset.toastDetail || "");
    });
});

document.querySelectorAll("[data-modal-title]").forEach((button) => {
    button.addEventListener("click", () => {
        openModal(button.dataset.modalTitle, button.dataset.modalMessage || "");
    });
});

document.querySelectorAll("form[data-loading-text]").forEach((form) => {
    form.addEventListener("submit", () => {
        const submitButton = form.querySelector('button[type="submit"]');

        if (!submitButton || submitButton.dataset.loadingApplied === "true") {
            return;
        }

        submitButton.dataset.loadingApplied = "true";
        submitButton.dataset.originalText = submitButton.textContent;
        submitButton.textContent = form.dataset.loadingText;
        submitButton.disabled = true;
    });
});

document.querySelectorAll(".flash").forEach((flash, index) => {
    window.setTimeout(() => {
        flash.classList.add("flash-hidden");
        window.setTimeout(() => flash.remove(), 260);
    }, 3800 + index * 180);
});

if (modalClose) {
    modalClose.addEventListener("click", closeModal);
}

if (modal) {
    modal.addEventListener("click", (event) => {
        if (event.target === modal) {
            closeModal();
        }
    });
}

document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
        closeModal();
    }
});
