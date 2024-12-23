# Using BronKerbosch algorithm

use strict;
use warnings;

sub part2 {

    my @puzzle_input = @_;
    my %computers    = ();
    my %connections  = ();

    for my $line (@puzzle_input) {
        my ( $a, $b ) = split /-/sxm, $line;
        $computers{$a}        = 1;
        $computers{$b}        = 1;
        $connections{"$a,$b"} = 1;
        $connections{"$b,$a"} = 1;
    }

    my @networks = map { [$_] } keys %computers;

    for my $network (@networks) {
        for my $a ( keys %computers ) {
            my $connected_to_all = 1;
            for my $b ( @{$network} ) {
                if ( !exists $connections{"$a,$b"} ) {
                    $connected_to_all = 0;
                    last;
                }
            }

            if ( $connected_to_all == 1 ) {
                push @{$network}, $a;
            }
        }
    }

    my @largest_network =
      @{ ( reverse sort { scalar @{$a} <=> scalar @{$b} } @networks )[0] };

    @largest_network = sort @largest_network;
    return join q{,}, @largest_network;

}

1;

