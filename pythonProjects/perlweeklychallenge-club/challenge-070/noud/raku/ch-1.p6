# You are given a string $S of size $N.
#
# You are also given swap count $C and offset $O such that $C >= 1, $O >= 1, $C
# <= $O and $C + $O <= $N.
#
# UPDATE: 2020-07-20 16:10:00
# Pete Houston suggested to put additional constraint i.e. $C <= $O. He
# presented the use case $S = 'abcd', $C = 2, $O = 1.
#
# Write a script to perform character swapping like below:
#
# $S[ 1 % $N ] <=> $S[ (1 + $O) % $N ]
# $S[ 2 % $N ] <=> $S[ (2 + $O) % $N ]
# $S[ 3 % $N ] <=> $S[ (3 + $O) % $N ]
# ...
# ...
# $S[ $C % $N ] <=> $S[ ($C + $O) % $N ]
#
# Example 1
#
# Input:
#     $S = 'perlandraku'
#     $C = 3
#     $O = 4
#
# Character Swapping:
#     swap 1: e <=> n = pnrlaedraku
#     swap 2: r <=> d = pndlaerraku
#     swap 3: l <=> r = pndraerlaku
#
# Output:
#     pndraerlaku


sub char-swap($S, $C, $O) {
    my $new-S = $S;
    for 1..$C -> $i {
        $new-S.substr-rw($i, 1) = $S.comb[$i + $O];
        $new-S.substr-rw($i + $O, 1) = $S.comb[$i];
    }
    return $new-S;
}

char-swap('perlandraku', 3, 4).say;
