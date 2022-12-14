from threading import Thread

points = [[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],[830,-417],[-870,73],[-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],[-839,-856],[-515,-447],[652,197],[-83,345],[-69,423],[310,-737],[78,-201],[443,958],[-311,988],[-477,30],[-376,-153],[-272,451],[322,-125],[-114,-214],[495,33],[371,-533],[-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],[315,27],[991,322],[811,-746],[252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],[-944,982],[937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]
# points.sort()
def calculate_time(points):
    time = 0
    current = points[0]
    for point in points[1:]:
        if current == point:
            continue

        elif current < point:
            while current < point:
                if current[0] < point[0] and current[1] < point[1]:
                    current[0] +=1
                    current[1] +=1
                    time +=1

                elif current[0] < point[0] and current[1] == point[1]:
                    current[0] +=1
                    time +=1

                elif current[0] == point[0] and current[1] < point[1]:
                    current[1] +=1
                    time +=1

            else:
                continue

        elif current > point:
            while current > point:
                if current[0] > point[0] and current[1] > point[1]:
                    current[0] -=1
                    current[1] -=1
                    time +=1

                elif current[0] > point[0] and current[1] == point[1]:
                    current[0] -=1
                    time +=1

                elif current[0] == point[0] and current[1] > point[1]:
                    current[1] -=1
                    time +=1

            else:
                continue
    return time
