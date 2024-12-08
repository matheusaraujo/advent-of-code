use strict;
use warnings;

sub part2 {
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
            if ( $word_search[$i][$j] eq 'A' ) {
                my $left_up =
                  ( $i > 0 && $j > 0 )
                  ? $word_search[ $i - 1 ][ $j - 1 ]
                  : q{};
                my $right_up =
                  ( $i > 0 && $j < $n )
                  ? $word_search[ $i - 1 ][ $j + 1 ]
                  : q{};
                my $left_down =
                  ( $i < $m && $j > 0 )
                  ? $word_search[ $i + 1 ][ $j - 1 ]
                  : q{};
                my $right_down =
                  ( $i < $m && $j < $n )
                  ? $word_search[ $i + 1 ][ $j + 1 ]
                  : q{};

                my $diagonal1 = $left_up . $right_down;
                my $diagonal2 = $right_up . $left_down;

                if (   ( $diagonal1 eq 'MS' || $diagonal1 eq 'SM' )
                    && ( $diagonal2 eq 'SM' || $diagonal2 eq 'MS' ) )
                {
                    $result++;
                }
            }
        }
    }
    return $result;
}

1;
