import NearestPoint
def main():
    points=[[-1,3],[-1,-1],[1,1],[2,0.5],[2,-1],[3,3],[4,2],[4,-0.5]]
    p1,p2=NearestPoint.nearestPoints(points)
    print(points[p1][0],points[p1][1],"===",points[p2][0],points[p2][1])


main()