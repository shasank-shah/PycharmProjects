#!/usr/bin/env raku

use v6;

# BTree as string nodevalue[child1,child2]
# Example tree 5(4(11(7)(2)))(8(13)(9(1)))

grammar BTreeGrammar {
    token TOP { <tree> };
    token tree { <value> ["(" $<left>=<tree> ")"]? ["(" $<right>=<tree> ")"]? };
    regex value { <-[()]>+ }
}

class BTreeRep {...}

role BTree[::T] {
    has T $.value is required;
    has BTree @!nodes[2];
    
    method Str( ) {
        ( $!value , |@.nodes.map( { "({$_})" } ) ).join("");
    }

    method nodes() {
        @!nodes.grep({defined $_});
    }

    method children() {
        @.nodes.elems;
    }

    method gist() {
        BTreeRep.new( tree=>self ).gist();
    }

    method traverse() {
        gather {
            if ( self.children ) {
                for @.nodes -> $n {
                    for $n.traverse -> @t {
                        take ($!value, |@t);
                    }
                }
            } else {
                take ( $!value, );
            }
        }
    }

    multi method reverse( ::?CLASS:D: ) {
        self.new(
            value => $!value,
            nodes => @.nodes.reverse.map( *.reverse )
        )
    }
    
    multi method from-Str('') { BTree }

    multi method from-Str( ::?CLASS:U: Str $in ) {
        my $match = BTreeGrammar.parse( $in );
        if ( $match ) {
            self.new(
                value => $match<tree><value>.Str,
                nodes => [
                          self.from-Str( $match<tree><left> ?? $match<tree><left>.Str !! '' ),
                          self.from-Str( $match<tree><right> ?? $match<tree><right>.Str !! '' )
                      ]
            );
        } else {
            die "Unable to Parse $in";
        }
            
    }
}

class UBTree does BTree[UInt] {
    submethod BUILD ( UInt() :$value, :@nodes ) {
        $!value = $value;
        @!nodes = @nodes;
    }
}

class BTreeRep {
    has @.data;
    has UInt $.join-point;

    multi submethod BUILD ( BTree :$tree where { ! $tree.children } ) {
            @!data = [$tree.value.Str];
            $!join-point = $tree.value.Str.codes div 2;
    }

    multi submethod BUILD ( BTree :$tree ) {
        my ( $left, $right, $left-width, $right-width );
        my ( @ldata, @rdata, $left-pad, $right-pad );

        my $mid-string = '┘';
        $left = BTreeRep.new( tree => $tree.nodes[0] );
        $left-width = $left.data[0].codes;
        @ldata = $left.data;
        @ldata.unshift( (" " x $left.join-point) ~ "┌" ~ ("─" x ($left-width - 1 - $left.join-point) ) );

        if ( $tree.children == 2 ) {
            my $right = BTreeRep.new( tree => $tree.nodes[1] );
            $mid-string = '┴';
            @rdata = $right.data;
            $right-width = @rdata[0].codes;
            @rdata.unshift( ( "─" x ( $right.join-point ) ~ '┐' ~ ( " " x $right-width - 1 - $right.join-point ) ) );
        } else {
            $right-width = 1;
            @rdata = @ldata.map( { " " } );
        }

        if ( $left-width + $right-width + 1 < $tree.value.codes ) {
            $left-pad = 0;
            $right-pad = 0;
            my $extra = $tree.value.codes - ($left-width + $right-width + 1);
            @ldata = @ldata.map( { ( " " x ( $extra div 2 ) ) ~ $_ } );
            @rdata = @rdata.map( { $_ ~ ( " " x ( $extra div 2 + $extra % 2 ) ) } );
        } else {
            $left-pad = $left-width - ($tree.value.codes div 2);
            $right-pad = ($left-width + $right-width + 1) - $left-pad - $tree.value.codes;
        }
        my $top = ( " " x $left-pad ) ~ $tree.value ~ ( " " x $right-pad );
        my $left-fill = gather { for @ldata.elems^..@rdata.elems { take " " x $left-width } };
        my $right-fill = gather { for @rdata.elems^..@ldata.elems { take " " x $right-width } };

        @!data = $top, |( ( (|@ldata, |$left-fill) Z, (|@rdata, |$right-fill) ).map( { state $i=0;$_.join($i++??" "!!$mid-string) } ) );
        $!join-point = $left-pad + ( $tree.value.Str.codes div 2);
    }

    method gist {
        @.data.join("\n");
    }

}

#| Given a tree string prints it then reverses all the nodes and reprints it
#| Note the Tree string is in the format "number (left tree) (right tree)" spaces are optional
multi sub MAIN ( *@rest ) {
    my $tree = UBTree.from-Str( @rest.join("") );
    say "Tree :\n{$tree.gist}\n";
    say "Reversed :\n{$tree.reverse.gist}\n";
}
