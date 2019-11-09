import visdom
import numpy as np
viz=visdom.Visdom(env='TY',port=8097)

my_win = viz.line(X = np.array([0]),
                  Y = np.column_stack((0,0,0,0)),
                  opts = {
                        'title': 'Viz_line_test', 'xlabel': 'iterations', 'ylabel': 'losses',
                        'width': 600, 'height': 600, 'marginleft': 30, 'marginbottom': 30,
                        'dash': np.array(['solid','dot','dash','dashdot']),
                        'linecolor': np.array([[0,0,255], [0,255,0],[255,0,0],[135,125,125]]),
                        'legend':['rpn_cls','rpn_reg','rcnn_cls','rcnn_reg'],
                        'showlegend':True, }                        
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
'''
中间那个 opts字典也可以用 dict( )函数来创建，上面是直接输入成字典，感觉手打有点慢，因为要不停的加单引号，下面的直接用等号，显得美观一些
my_win = viz.line(X = np.array([0]),
                  Y = np.column_stack((0,0,0,0)),
                  opts = dict(
                        title = 'Viz_line_test', xlabel = 'iterations', ylabel = 'losses',
                        width = 600, height = 600, marginleft = 30, marginbottom = 30,
                        dash = np.array(['solid','solid','dash','dashdot']),
                        linecolor = np.array([[0,0,230], [0,180,180],[255,0,0],[135,125,125]]),
                        legend = ['rpn_cls','rpn_reg','rcnn_cls','rcnn_reg'],
                        showlegend = True, )                        
                        )
'''
