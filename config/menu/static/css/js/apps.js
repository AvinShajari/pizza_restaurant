function filterProducts(categoryId, button) {

    const products = document.querySelectorAll(".product-card");
    const buttons = document.querySelectorAll(".category-button");

    // دکمه فعال
    buttons.forEach(function (btn) {
        btn.classList.remove("active");
    });

    button.classList.add("active");

    // تبدیل به رشته
    const selectedCategory = String(categoryId).trim();

    products.forEach(function (product) {

        const productCategory = String(
            product.dataset.category
        ).trim();

        if (selectedCategory === "all") {

            product.style.display = "";

        } else if (productCategory === selectedCategory) {

            product.style.display = "";

        } else {

            product.style.display = "none";

        }

    });
}