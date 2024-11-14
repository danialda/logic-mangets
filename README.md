node.py : هو عبارة عن تمثيل لكل حالة من حالات اللعبة
logic.py : "يمثل تاثير كل من الكرتين الحمراء والبنفسجية على المصفوفة "الرقعة
init_states_of_cells.py : "لدينا مجموعة من المصفوفات التي تمثل توزيع الكرات على الرقعة "الحالات البدائية

///////////////////////////

لدي ضمن بنية كل رقعة :

targetCells: التي تمثل موقع جميع الخلايا الهدف
emptyCells: تمثل مواقع جميع الخلايا التي لا تحتوي على كرات 
magnetBalls:  تمثل مواقع جميع الكرات المغناطيسية 
normalBalls: تمثل مواقع جميع الكرات الغير مغناطيسية

لكل حالة والذي يحتوي على المصفوفة الخاصة بكل حالة وكل خلية ضمن هذه المصفوفة عبارة عن Board لدينا ايضا
cell: bath or target 
ball: red or red or purpule or none

نستطيع اختيار اي مصفوفة من المصفوفات البدائية , في مثالنا 
        [init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none)],
        [init_B_C(Ball.none),init_B_C(Ball.none,True),init_B_C(Ball.grey),init_B_C(Ball.none,True)],
        [init_B_C(Ball.purpule),init_B_C(Ball.none),init_B_C(Ball.none),init_B_C(Ball.none)],
init_B_C(): يعيد كل خلية عبار عن {ball:__ , cell:___}         
init_B_C(Ball.none): تمثل انه لا توجد كرة والخلية ليست هدف
init_B_C(Ball.none,True): True تعني ان هذه الخلية هدف

تحتوي على كراتtarget ونستطيع معرفة ان الحالة هي حالة النهائسة عن طريق التحقق من ان جميع الخلايا ال

