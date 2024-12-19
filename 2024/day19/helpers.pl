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

1;
