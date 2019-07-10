from manimlib.imports import *

def doubling_line(x):
    return 2*x

def hidden_flat_line(x):
    return 0

def parabola(x):
    return x**2


class LinearIsInvertible(GraphScene):
    CONFIG = {
        "x_min" : -5.5,
        "x_max" : 5.5,
        "y_min" : -11,
        "y_max" : 11,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,1),
        "center_point" : 0
    }   
    
    def construct(self):
        self.setup_axes(animate=True)
        
        graph_object = self.get_graph(hidden_flat_line,self.function_color)
        line_obj = self.get_graph(doubling_line,self.function_color)
        vert_line = self.get_vertical_line_to_graph(2,line_obj,color=YELLOW) #this might be made to go to graph_obj if you use ReplacementTransform in previous line
        hori_line = self.get_graph(lambda x : 4, color = YELLOW, x_min = 2, x_max = 0) #reversing axes works exactly the way i want here
        
        self.play(ShowCreation(graph_object))
        self.play(Transform(graph_object,line_obj))
        self.play(ShowCreation(vert_line))
        self.wait()
        self.play(ShowCreation(hori_line))

class ParabolaNotInvertible(GraphScene):
    CONFIG = {
        "x_min" : -5.5,
        "x_max" : 5.5,
        "y_min" : -11,
        "y_max" : 11,
        "graph_origin" : ORIGIN ,
        "function_color" : BLUE ,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,1),
        "center_point" : 0
    }   
    
    def construct(self):
        self.setup_axes(animate=True)
        graph_object = self.get_graph(hidden_flat_line,self.function_color)
        parabola_obj = self.get_graph(parabola,self.function_color)
        
        #vert_line = self.get_vertical_line_to_graph(2,line_obj,color=YELLOW)
        hori_line_to_right = self.get_graph(lambda x : 4, color = YELLOW, x_min = 0, x_max = 2)
        hori_line_to_left = self.get_graph(lambda x : 4, color = YELLOW, x_min = 0, x_max = -2)
        #vert_line_right = self.get_vertical_line_to_graph(2,sneaky_line_obj)
        
        vert_line_right = Line(self.coords_to_point(2, 4), self.input_to_graph_point(2, graph_object),color =YELLOW)
        vert_line_left = Line(self.coords_to_point(-2, 4), self.input_to_graph_point(-2, graph_object),color =YELLOW)
        
        self.play(ShowCreation(graph_object))
        self.play(Transform(graph_object,parabola_obj))
        
        self.wait()
        self.play(ShowCreation(hori_line_to_right),ShowCreation(hori_line_to_left))        
        self.play(ShowCreation(vert_line_right),ShowCreation(vert_line_left))