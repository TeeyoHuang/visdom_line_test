import visdom
import numpy as np
viz=visdom.Visdom(env='Faster_RCNN_Test_4',port=8097)

my_win = viz.line(X = np.array([0]),
                  Y = np.column_stack((0,0,0,0)),
                  opts = {
                        'width':600,
                        'height':600,
                        'marginleft':30,
                        'marginbottom':30,
                        'dash': np.array(['solid','solid','dash','dashdot']),
                        'linecolor': np.array([[0,0,255], [0,255,0],[255,0,0],[135,125,125]]),
                        'title':'Faster_RCNN_Test_4',
                        'xlabel':'iterations',
                        'ylabel':'losses',
                        'showlegend':True,
                        'legend':['rpn_cls','rpn_reg','rcnn_cls','rcnn_reg'],}
                        )

viz.line(win=my_win,
                 X = np.array([1]),
                 Y = np.column_stack(( 1, 2,
                                        3, 4 )),
                  update = 'append')

viz.line(win=my_win,
                 X = np.array([2]),
                 Y = np.column_stack(( 2, 4,
                                        6, 8 )),
                  update = 'append')
