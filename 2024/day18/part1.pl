use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my %corrupted    = ();
    my $count        = 0;

    for my $line (@puzzle_input) {
        my ( $x, $y ) = split /,/smx, $line;
        $corrupted{"$x,$y"} = 1;
        $count++;
        if ( $count == 1024 ) {
            last;
        }
    }

    return dfs( 71, \%corrupted );
}

1;
