##
# Write a script to print the smallest pair of Amicable Numbers.
##
constant RANGE_SIZE = 50; 
sub factor-sum(@numbers){
    my %number_sof;
    for @numbers -> $n {
        my @factors = (1);
        for (2 .. sqrt($n)) -> $j {
            @factors.push($j) if $n %% $j;
            @factors.push($n / $j) if $n %% $j && $j ** 2 != $n;
        }
        my $sum = [+] @factors;  
        %number_sof{$n} = $sum; 
    }
    return %number_sof;
}  
my $range_start = 1;
my $range_end = RANGE_SIZE; 
my $found = Bool::False;
my %number_sof; 
my @promises;
while (!$found) {
    @promises = ();
    for (0 .. 3) {
        @promises.push(Promise.start( {
            factor-sum($range_start .. $range_end);  
        }));      
        $range_start = $range_end + 1;
        $range_end = $range_start + RANGE_SIZE;
    }  
    await(|@promises);  
    for @promises -> $p {
        %number_sof{ keys $p.result} = values $p.result;
        for (values $p.result) -> $k {
            if (%number_sof{$k}) {
                    if (%number_sof{%number_sof{$k}} &&
                       %number_sof{%number_sof{$k}} == $k &&
                       %number_sof{$k} != $k && !$found) {
                           say "First amicable pair of numbers: $k " ~ %number_sof{$k};
                           $found = Bool::True;
                    }
            }
        } 
    }  
}  
