# WARNING: this polyglot breaks best practices of both Perl 5 and Perl 6 in order to run on both

my @ARGV = do { sub eval($_) { &EVAL($_) }; eval( ("0" and q|@*ARGS| or q|@ARGV|) ) }; print("$_\n") for map &{ sub ($_) { /^0(0|1|2|3|4|5|6|7|8|9)+/ and (0+$_) or $_ } }.(), @ARGV;
