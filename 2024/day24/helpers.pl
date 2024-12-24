use strict;
use warnings;

sub parse_input {
    my @puzzle_input = @_;
    my $i            = 0;
    my %wires        = ();
    my %operations   = ();

    while ( $puzzle_input[$i] ) {
        my ( $wire, $value ) = split /:\s/sxm, $puzzle_input[$i];
        $wires{$wire} = $value;
        $i++;
    }
    $i++;

    while ( $puzzle_input[$i] ) {
        my ( $op1, $operation, $op2, undef, $wire ) = split /\s/sxm,
          $puzzle_input[$i];
        $puzzle_input[$i];

        $operations{$wire} = [ $op1, $operation, $op2, $wire ];

        if ( !exists $wires{$wire} ) {
            $wires{$wire} = -1;
        }
        if ( !exists $wires{$op1} ) {
            $wires{$op1} = -1;
        }
        if ( !exists $wires{$op2} ) {
            $wires{$op2} = -1;
        }

        $i++;
    }

    return \%wires, \%operations;
}

1;
