use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;
    my $size         = $#puzzle_input;

    foreach my $i ( 0 .. $size ) {
        foreach my $j ( $i + 1 .. $size ) {

            my $diff = 0;
            my $common;
            foreach my $k ( 0 .. length( $puzzle_input[$i] ) - 1 ) {

                if ( ( substr $puzzle_input[$i], $k, 1 ) ne
                    ( substr $puzzle_input[$j], $k, 1 ) )
                {
                    $diff++;
                }
                else {
                    $common .= substr $puzzle_input[$i], $k, 1;
                }

            }
            if ( $diff == 1 ) {
                return $common;
            }
        }
    }

    return 'not found';
}

1;

