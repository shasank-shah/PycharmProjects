#!/usr/bin/env raku

sub MAIN(Str $operand1,Str $operator,Str $operand2){
	#convert to decimal
	my ($o1,$o2)=($operand1,$operand2).map({ 
		when /<[MDCLXVI]>/ {romanToDecimal($_)};
		 when /\d+/ {$_};
		"Not a digit or roman numeral";
	});
	my $result= do { 
		given $operator {
			when "+" {$o1+$o2};
			when "-" {$o1-$o2};
			when "/" {Int($o1/$o2)};
			when "*" {$o1*$o2};
			"Unknown";
		}
	};
	put decimalToRoman($result);

}
sub decimalToRoman ($input) {
	my @digits=$input.comb;
	my @p=<I X C M>;
	my @h=<V L D>;
	my $roman= join '', do for  @digits.kv {
		my $power=@digits-$^k-1;	
		#decimalToRoman($^v,@digits-$^k-1);
		my @out;
		my $base=@p[$power];
		my $half=@h[$power];
		given $^v {
			when 1..3 {
				@out.append: $base xx $_;
			}
			when 4 {
				@out.push: $base;
				@out.push: $half;
			}
			when 5 {
				@out.push: $half;
			}
			when 6..8 {
				@out.push: $half;
				@out.append: $base xx ($_- 5);
			}
			when 9 {
				@out.push: $base;
				@out.push: @p[$power+1];
			}

		}
		|@out;
	}
}

sub romanToDecimal($input) {

	my %r=(M=>1000, C=>100 ,X=>10, I=>1, V=>5, L=>50, D=>500);
	my @order=%r.sort: *.value <=> *.value;
	my @c=$input.comb;
	my $diff=0;
	my $sum=0;

	for @c.kv -> $k, $v {
		if $k+1 < @c {
			if (%r{@c[$k+1]} > %r{$v}) {
				$diff=%r{$v};
			}
			else {
				$sum+=%r{$v}- $diff;
				$diff=0;
			}
		
		}
		else {
			$sum+=%r{$v}- $diff;
		}
	}
	$sum;
}

