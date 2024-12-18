# TODO: @matheusaraujo - brute force, this code needs to be refactored
# suggestion: use binary search to find the answer between 1024 and the end of the input

use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;

    for my $i ( 1024 .. $#puzzle_input ) {
        my $answer    = q{};
        my $count     = 0;
        my %corrupted = ();
        for my $line (@puzzle_input) {
            my ( $x, $y ) = split /,/smx, $line;
            $corrupted{"$x,$y"} = 1;
            $count++;
            if ( $count == $i ) {
                $answer = "$x,$y";
                last;
            }
        }

        if ( dfs( 71, \%corrupted ) == -1 ) {
            return $answer;
        }
    }
    return '-1,-1';
}

1;
