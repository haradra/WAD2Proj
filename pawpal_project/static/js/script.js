function selectButton(element) {
    $(element).parent().find("button").removeClass("active");
    $(element).addClass("active");
}