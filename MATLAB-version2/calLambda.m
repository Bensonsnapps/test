function la = calLambda(Pin, la, epsilon, y)
    la = la * Pin' + epsilon * y;
end
