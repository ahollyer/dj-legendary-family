$(document).ready(function () {
    var removeBtn = $(".remove")[0].outerHTML;
    var editBtn = $(".edit")[0].outerHTML;

    $(".add-button").click(function() {
      let item = $(".description").val();
      $(".description").val("");
      $("#todo-list").append("<li><input type='checkbox' class='check'><span> " + item + "</span> " + editBtn + " " + removeBtn + "</li>");
    });

    $("#todo-list").on("click", ".remove", function() {
      $(this).parent().remove();
    });

    $("#todo-list").on("click", ".check", function() {
      $(this).parent().toggleClass("strike");
    });

    $("#todo-list").on("click", ".edit", function() {
      let msg = $(this).prev().text();
      $(this).parent().replaceWith("<li><input type='text' value='" + msg + "'> <button class='edit-done'>Done Editing</button></li>");
    });

    $("#todo-list").on("click", ".edit-done", function() {
      let msg = $(this).prev().val();
      $(this).parent().replaceWith("<li><input type='checkbox' class='check'><span> " + msg + "</span> " + editBtn + " " + removeBtn + "</li>");
    });
});
