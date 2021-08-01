def better_than_average(class_points, your_points):
    # Your code here
    class_points = class_points
    class_points.append(your_points)  # add your points to class points
    
    avg_points = sum(class_points)/len(class_points)
    if your_points > avg_points:
        return True  # you're better!
    else:
        return False