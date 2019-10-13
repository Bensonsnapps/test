function y = calY(Qout, y, x, x_old, De, De_old, generator)
    y = y * Qout' - x + x_old;
    y(generator) = y(generator) + De - De_old;
end