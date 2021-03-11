/**
 * Created by shaoning on 2018/4/11.
 */
var mainShowBodyShowCodeManageCodeShowOnePart=$(".mainShowBodyShowCodeManageCodeShowOnePart");
mainShowBodyShowCodeManageCodeShowOnePart.alt=0;
mainShowBodyShowCodeManageCodeShowOnePart.click(function(){
    if(this.alt==undefined){
        //console.log(undefined);
        this.alt=0;
    }
    //console.log(this.alt);
    if(this.alt==0){
        $(this).css({
            "height":"500px"
        });
        //$($(this).children('div')[$(this).children('div').length-2]).removeClass("mainShowBodyShowCodeManageCodeShowOnePartResume_hide").addClass("mainShowBodyShowCodeManageCodeShowOnePartResume_show");
        $($(this).children('.mainShowBodyShowCodeManageCodeShowOnePartByTime')).stop().slideDown(500);
        this.alt=1;
        //console.log(this.id);
    }else{
        $(this).css({
            "height":"150px"
        });
        //$($(this).children('div')[$(this).children('div').length-2]).removeClass("mainShowBodyShowCodeManageCodeShowOnePartResume_show").addClass("mainShowBodyShowCodeManageCodeShowOnePartResume_hide");
        $($(this).children('.mainShowBodyShowCodeManageCodeShowOnePartByTime')).stop().slideUp(250);
        this.alt=0;
    }
});