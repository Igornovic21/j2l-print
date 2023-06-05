$(".image-carousel").click(function(){
    var url = $(this).attr("src");
    $("#cover").attr("src", url);
});