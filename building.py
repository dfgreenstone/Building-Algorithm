'''Lorenzo, Jonathan, Erasmo, Konstantinos and Clover like to take long walks
and discuss problems for next week. On one of those days, they were looking at
downtown Chicago from the Promontory Point in Hyde Park and were wondering how
an algorithm would construct a rendering of the view given information about the
location and height of the buildings. Thankfully, the student in Theory of
Algorithms can definitely help.

Assume every building is given as three integers $(left_i, width_i, height_i)$,
where $left_i$ indicates the distance at which building $i$ starts,  $width_i$
is the building's width and $height_i$ is its height. You need to return a list
of intervals $(x_j, h_j)$, denoting the distance at which $x_j$ which correspond
with where a height change starts and what the new height is.

{\\bf Input:}
The first line contains a single integer $N$, the number of buildings. $N$ lines
follow. Each line has three integers; where the building starts on the $x$-axis,
its width and its height. DO NOT ASSUME THEY ARE ORDERED.

{\\bf Output:}
You need to print out the height segments. In every line there should be two
integers. The first one designates where the segment starts and the second is the
height.'''


# Add your functions here


def solve(N, rectangles):
    leftborders = {-1: 0}
    rightborders = {0: 0}
    intervals = []
    for rec in rectangles:
        leftborders[rec[0]] = rec[2]
        rightborders[rec[0] + rec[1]] = rec[2]
    for i in leftborders:
        if(i in rightborders):
            intervals.append((i, abs(leftborders[i] - rightborders[i])))



def print_solution(intervals):
    for x, h in intervals:
        print(x, h)


def main():
    N = int(input())
    rectangles = [[int(i) for i in input().split()] for _ in range(N)]
    intervals = solve(N, rectangles)
    print_solution(intervals)


if __name__ == '__main__':
    main()
