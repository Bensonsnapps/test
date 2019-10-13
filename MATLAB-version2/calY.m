function y = calY(Qout, y, x, x_old, De, De_old, group)
    y = y * Qout' - x + x_old;
    %y(group) = y(group) + De - De_old;
end