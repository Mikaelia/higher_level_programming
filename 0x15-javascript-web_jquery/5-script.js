let list = $("UL.my_list");

$("DIV#add_item").click(function () {
    let elem = "<li>Item</li>";
    list.append(elem);
})