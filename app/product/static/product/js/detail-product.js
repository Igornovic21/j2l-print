$(".image-carousel").click(function() {
    const url = $(this).attr("src");
    $("#cover").attr("src", url);
});

selected_checkbox = []

$("input[type='checkbox']").click(function() {
    const is_checked = $(this).is(":checked");
    const name = $(this).attr("name");

    if (is_checked) {
        $(`div[id=${name}]`).removeClass("d-none");
        selected_checkbox.push(name);
    } else {
        $(`div[id=${name}]`).addClass("d-none");
        const index = selected_checkbox.indexOf(name);
        selected_checkbox.splice(index, 1);
    }
    
    if (selected_checkbox.length === 0) {
        $("hr").removeClass("d-block");
        $("hr").addClass("d-none");
    } else {
        $("hr").removeClass("d-none");
        $("hr").addClass("d-block");
    }
})