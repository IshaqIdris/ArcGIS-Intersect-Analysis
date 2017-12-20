# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

#check intersections betweeen features
def intersect_analysis():
    #The features you want to see if they intersect
    inFeatures = ["SWNode", "buffer"]
    #output features to another feature class
    intersect_output = "river_road_intersects"
    arcpy.Intersect_analysis(inFeatures, intersect_output)


# Set environment settings
env.workspace = "C:/Practice map/YOUR.gdb"

intersect_analysis()
