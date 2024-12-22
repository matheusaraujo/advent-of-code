use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my ( $count2, $count3 ) = ( 0, 0 );

    foreach my $word (@puzzle_input) {
        my %letters;
        foreach my $letter ( split //sm, $word ) {
            $letters{$letter}++;
        }
        my ( $has2, $has3 ) = ( 0, 0 );

        foreach my $letter ( keys %letters ) {
            if ( $letters{$letter} == 2 ) {
                $has2 = 1;
            }
            if ( $letters{$letter} == 3 ) {
                $has3 = 1;
            }
        }
        $count2 += $has2;
        $count3 += $has3;
    }

    return $count2 * $count3;
}

1;
