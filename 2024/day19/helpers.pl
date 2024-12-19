use strict;
use warnings;

sub parse_input {
    my @puzzle_input = @_;
    my %patterns     = ();
    my @designs      = ();

    for ( split /,\s/smx, $puzzle_input[0] ) {
        $patterns{$_} = 1;
    }

    for my $i ( 2 .. $#puzzle_input ) {
        push @designs, $puzzle_input[$i];
    }

    return ( \%patterns, \@designs );
}

sub count_ways {
    my ( $design, $patterns ) = @_;

    my @dp = (0) x ( length($design) + 1 );
    $dp[0] = 1;

    for my $i ( 1 .. length $design ) {
        for my $j ( 0 .. $i - 1 ) {
            my $substring = substr $design, $j, $i - $j;
            if ( $dp[$j] && exists $patterns->{$substring} ) {
                $dp[$i] += $dp[$j];
            }
        }
    }

    return $dp[ length $design ];
}

1;
