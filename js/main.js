document.documentElement.classList.add("js");

const menuButton = document.querySelector(".menu-toggle");
const siteNav = document.querySelector(".site-nav");

function closeMenu() {
  if (!menuButton || !siteNav) return;
  menuButton.setAttribute("aria-expanded", "false");
  menuButton.setAttribute("aria-label", "Open menu");
  siteNav.classList.remove("is-open");
}

menuButton?.addEventListener("click", () => {
  const isOpen = menuButton.getAttribute("aria-expanded") === "true";
  menuButton.setAttribute("aria-expanded", String(!isOpen));
  menuButton.setAttribute("aria-label", isOpen ? "Open menu" : "Close menu");
  siteNav?.classList.toggle("is-open", !isOpen);
});

siteNav?.querySelectorAll("a").forEach((link) => link.addEventListener("click", closeMenu));
document.addEventListener("click", (event) => {
  if (
    menuButton?.getAttribute("aria-expanded") === "true" &&
    !siteNav?.contains(event.target) &&
    !menuButton?.contains(event.target)
  ) {
    closeMenu();
  }
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && menuButton?.getAttribute("aria-expanded") === "true") {
    closeMenu();
    menuButton.focus();
  }
});

window.addEventListener("resize", () => {
  if (window.matchMedia("(min-width: 701px)").matches) closeMenu();
});

const serviceDialog = document.querySelector("#service-contact-dialog");
const serviceEmailLink = document.querySelector("#service-dialog-email");
const serviceName = document.querySelector("#service-dialog-name");
const serviceDialogClose = serviceDialog?.querySelector(".service-dialog-close");

if (serviceDialog && serviceEmailLink && serviceName) {
  document.querySelectorAll(".service-contact-trigger").forEach((trigger) => {
    trigger.addEventListener("click", () => {
      const service = trigger.dataset.service || "vehicle service";
      serviceName.textContent = service;
      serviceEmailLink.href = `mailto:automatelankanz@gmail.com?subject=${encodeURIComponent(`Vehicle service enquiry: ${service}`)}`;
      serviceDialog.showModal();
      serviceEmailLink.focus({ preventScroll: true });
    });
  });

  serviceDialogClose?.addEventListener("click", () => serviceDialog.close());
  serviceDialog.querySelectorAll(".service-dialog-option").forEach((option) => {
    option.addEventListener("click", () => serviceDialog.close());
  });
  serviceDialog.addEventListener("click", (event) => {
    if (event.target === serviceDialog) serviceDialog.close();
  });
}

const year = document.querySelector("#year");
if (year) year.textContent = new Date().getFullYear();

const revealItems = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  revealItems.forEach((item) => revealObserver.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}
