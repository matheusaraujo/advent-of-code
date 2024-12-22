use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my $result       = 0;
    my @xmas         = qw( X M A S );
    my @directions   = (
        [ -1, -1 ], [ -1, 0 ],  [ -1, 1 ], [ 0, -1 ],
        [ 0,  1 ],  [ 1,  -1 ], [ 1,  0 ], [ 1, 1 ],
    );

    my @word_search = parse_input(@puzzle_input);

    my ( $m, $n ) = ( $#word_search, $#{ $word_search[0] } );

    for my $i ( 0 .. $m ) {
        for my $j ( 0 .. $n ) {
            foreach my $dir (@directions) {
                my ( $dx, $dy ) = @{$dir};
                my ( $x,  $y )  = ( $i, $j );
                my $found = 1;
                for my $k ( 0 .. 3 ) {
                    if (   $x < 0
                        || $x > $m
                        || $y < 0
                        || $y > $n
                        || $word_search[$x][$y] ne $xmas[$k] )
                    {
                        $found = 0;
                        last;
                    }
                    $x += $dx;
                    $y += $dy;
                }
                $result += $found;
            }
        }
    }
    return $result;
}

1;
