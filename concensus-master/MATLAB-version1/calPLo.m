function P_Ls = calPLo(n_gen, P_load, group)
    P_Ls = zeros(1, n_gen);
    for i=1:length(group)
        P_Ls(group(i)) = P_Ls(group(i)) + P_load(i);
    end
end