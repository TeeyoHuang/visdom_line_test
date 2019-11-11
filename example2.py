

import visdom

viz=visdom.Visdom(env='Example_2', port=8097)
vis_tool = Visdom_tools(viz)






class Visdom_tools():
    def __init__(self, viz):
        self.viz = viz

    def initialize(self, first_loss):
        self.vis_window = self.viz.line(X=np.array([1]), Y=np.column_stack(first_loss),
                                        opts = dict(
                                        title = 'Loss_Map',
                                        xlabel = 'iterations', ylabel = 'Loss_values',
                                        width = 600, height = 300, marginleft = 30, marginbottom = 40,

                                        dash = np.array(['solid', 'solid', 'dash', 'dash', 'dot']),
                                        linecolor = np.array([ [0,0,230], [135,206,235], [255,0,0],[255,105,180],[0,0,0]]),
                                        legend = ['rpn_cls','rpn_reg','rcnn_cls','rcnn_reg','total_loss'], showlegend=True )
                                        )

    def draw_loss_lines(self, iter, loss_for_print):
        self.viz.line(X=np.array([iter]), Y=np.column_stack(loss_for_print),
                      win = self.vis_window,
                      update = 'append',
                      )
