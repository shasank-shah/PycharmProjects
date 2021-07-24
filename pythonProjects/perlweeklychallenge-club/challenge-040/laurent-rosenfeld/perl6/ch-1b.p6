use v6;

my @a = < I L O V E Y O U >,
        < 244 42 0 1233 222 0 11 >,
        < ! ???? £ $ %% ^ & * >,
        < a b c d e f g f i j>;

my $max = max map { .elems }, @a;
my @b = map { (| $_, "" xx $max - .elems).flat }, @a;
my @c = [Z] @b;
say join "\t", map {$_ // "" }, @$_ for @c;
