use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my ( $i, $result, $base ) = ( 0, 0, 1 );
    my ( $wires, $operations ) = parse_input(@puzzle_input);

    while (1) {
        my $id = sprintf 'z%02d', $i;

        if ( !exists $wires->{$id} ) {
            last;
        }

        if ( solve( $id, $wires, $operations ) ) {
            $result += $base;
        }
        $i++;
        $base *= 2;
    }

    return $result;
}

sub solve {
    my ( $wire, $wires, $operations ) = @_;
    if ( exists $wires->{$wire} && $wires->{$wire} != -1 ) {
        return $wires->{$wire};
    }
    my ( $op1, $operation, $op2, undef ) = @{ $operations->{$wire} };
    my $v1    = solve( $op1, $wires, $operations );
    my $v2    = solve( $op2, $wires, $operations );
    my $value = -1;

    if ( $operation eq 'AND' ) {
        $value = $v1 && $v2;
    }
    elsif ( $operation eq 'OR' ) {
        $value = $v1 || $v2;
    }
    elsif ( $operation eq 'XOR' ) {
        $value = $v1 ^ $v2;
    }
    $wires->{$wire} = $value;

    return $value;
}

1;
