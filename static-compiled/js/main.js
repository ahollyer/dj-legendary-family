$(document).ready(function () {

/*Fixed navbar behavior, adapted from cesiztel at Bootsnipp*/
var myNavBar = {

    flagAdd: true,

    elements: [],

    init: function (elements) {
        this.elements = elements;
    },

    add : function() {
        if(this.flagAdd) {
            for(var i=0; i < this.elements.length; i++) {
                document.getElementById(this.elements[i]).className += " fixed-theme";
            }
            this.flagAdd = false;
        }
    },

    remove: function() {
        for(var i=0; i < this.elements.length; i++) {
            document.getElementById(this.elements[i]).className =
                    document.getElementById(this.elements[i]).className.replace( /(?:^|\s)fixed-theme(?!\S)/g , '' );
        }
        this.flagAdd = true;
    }

};
/*Init the object. Pass the object the array of elements
 *that we want to change when the scroll goes down*/
myNavBar.init(  [
    "header",
    "header-container",
    "brand-name"
]);

/*Function that manages direction of scroll*/
function offSetManager(){

    var yOffset = 0;
    var currYOffSet = window.pageYOffset;

    if(yOffset < currYOffSet) {
        myNavBar.add();
    }
    else if(currYOffSet == yOffset){
        myNavBar.remove();
    }

}
/*Bind to the document scroll detection*/
window.onscroll = function(e) {
    offSetManager();
};
/*First detection of offset because the page could be loaded with scroll down set.*/
offSetManager();

});
