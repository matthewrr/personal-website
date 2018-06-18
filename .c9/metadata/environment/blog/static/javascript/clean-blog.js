{"filter":false,"title":"clean-blog.js","tooltip":"/blog/static/javascript/clean-blog.js","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["!function(i){\"use strict\";i(\"body\").on(\"input propertychange\",\".floating-label-form-group\",function(o){i(this).toggleClass(\"floating-label-form-group-with-value\",!!i(o.target).val())}).on(\"focus\",\".floating-label-form-group\",function(){i(this).addClass(\"floating-label-form-group-with-focus\")}).on(\"blur\",\".floating-label-form-group\",function(){i(this).removeClass(\"floating-label-form-group-with-focus\")});if(i(window).width()>992){var o=i(\"#mainNav\").height();i(window).on(\"scroll\",{previousTop:0},function(){var s=i(window).scrollTop();s<this.previousTop?s>0&&i(\"#mainNav\").hasClass(\"is-fixed\")?i(\"#mainNav\").addClass(\"is-visible\"):i(\"#mainNav\").removeClass(\"is-visible is-fixed\"):s>this.previousTop&&(i(\"#mainNav\").removeClass(\"is-visible\"),s>o&&!i(\"#mainNav\").hasClass(\"is-fixed\")&&i(\"#mainNav\").addClass(\"is-fixed\")),this.previousTop=s})}}(jQuery);",""],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["!function(i){\"use strict\";i(\"body\").on(\"input propertychange\",\".floating-label-form-group\",function(o){i(this).toggleClass(\"floating-label-form-group-with-value\",!!i(o.target).val())}).on(\"focus\",\".floating-label-form-group\",function(){i(this).addClass(\"floating-label-form-group-with-focus\")}).on(\"blur\",\".floating-label-form-group\",function(){i(this).removeClass(\"floating-label-form-group-with-focus\")});if(i(window).width()>992){var o=i(\"#mainNav\").height();i(window).on(\"scroll\",{previousTop:0},function(){var s=i(window).scrollTop();s<this.previousTop?s>0&&i(\"#mainNav\").hasClass(\"is-fixed\")?i(\"#mainNav\").addClass(\"is-visible\"):i(\"#mainNav\").removeClass(\"is-visible is-fixed\"):s>this.previousTop&&(i(\"#mainNav\").removeClass(\"is-visible\"),s>o&&!i(\"#mainNav\").hasClass(\"is-fixed\")&&i(\"#mainNav\").addClass(\"is-fixed\")),this.previousTop=s})}}(jQuery);",""],"id":4},{"start":{"row":0,"column":0},"end":{"row":40,"column":32},"action":"insert","lines":["(function($) {","  \"use strict\"; // Start of use strict","","  // Floating label headings for the contact form","  $(\"body\").on(\"input propertychange\", \".floating-label-form-group\", function(e) {","    $(this).toggleClass(\"floating-label-form-group-with-value\", !!$(e.target).val());","  }).on(\"focus\", \".floating-label-form-group\", function() {","    $(this).addClass(\"floating-label-form-group-with-focus\");","  }).on(\"blur\", \".floating-label-form-group\", function() {","    $(this).removeClass(\"floating-label-form-group-with-focus\");","  });","","  // Show the navbar when the page is scrolled up","  var MQL = 992;","","  //primary navigation slide-in effect","  if ($(window).width() > MQL) {","    var headerHeight = $('#mainNav').height();","    $(window).on('scroll', {","        previousTop: 0","      },","      function() {","        var currentTop = $(window).scrollTop();","        //check if user is scrolling up","        if (currentTop < this.previousTop) {","          //if scrolling up...","          if (currentTop > 0 && $('#mainNav').hasClass('is-fixed')) {","            $('#mainNav').addClass('is-visible');","          } else {","            $('#mainNav').removeClass('is-visible is-fixed');","          }","        } else if (currentTop > this.previousTop) {","          //if scrolling down...","          $('#mainNav').removeClass('is-visible');","          if (currentTop > headerHeight && !$('#mainNav').hasClass('is-fixed')) $('#mainNav').addClass('is-fixed');","        }","        this.previousTop = currentTop;","      });","  }","","})(jQuery); // End of use strict"]}]]},"ace":{"folds":[],"scrolltop":353,"scrollleft":0,"selection":{"start":{"row":40,"column":32},"end":{"row":40,"column":32},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":123,"mode":"ace/mode/javascript"}},"timestamp":1528850042884,"hash":"61d0606a02906fa63e57a175de0a12fcbec2ae31"}