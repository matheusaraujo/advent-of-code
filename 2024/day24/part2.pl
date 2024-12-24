# Counting wrong connections, based on https://www.reddit.com/r/adventofcode/comments/1hl698z/comment/m3kt1je/

use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;
    my %wrong;

    my ( $wires, $operations ) = parse_input(@puzzle_input);
    my $highest_z = find_highest_z_wire($wires);

    foreach my $operation ( values %{$operations} ) {
        my ( $op1, $op, $op2, $res ) = @{$operation};

        if ( is_invalid_z_connection( $op, $res, $highest_z ) ) {
            $wrong{$res} = 1;
        }
        if ( $op eq 'XOR' && is_invalid_xor( $op1, $op2, $res ) ) {
            $wrong{$res} = 1;
        }
        if ( $op eq 'AND'
            && is_invalid_and( $op1, $op2, $operations, $res ) )
        {
            $wrong{$res} = 1;
        }
        if ( $op eq 'XOR' && is_invalid_xor_or( $operations, $res ) ) {
            $wrong{$res} = 1;
        }
    }

    return join q{,}, sort keys %wrong;
}

sub is_invalid_z_connection {
    my ( $op, $res, $highest_z ) = @_;
    return ( $res =~ /^z/sxm && $op ne 'XOR' && $res ne $highest_z );
}

sub is_invalid_xor {
    my ( $op1, $op2, $res ) = @_;
    return ( $res !~ /^[xyz]/sxm
          && $op1 !~ /^[xyz]/sxm
          && $op2 !~ /^[xyz]/sxm );
}

sub is_invalid_and {
    my ( $op1, $op2, $operations, $res ) = @_;
    return !( $op1 eq 'x00' || $op2 eq 'x00' )
      && is_related_to_non_or( $operations, $res );
}

sub is_related_to_non_or {
    my ( $operations, $res ) = @_;
    foreach my $sub_operation ( values %{$operations} ) {
        my ( $sub_op1, $sub_op, $sub_op3, $sub_res ) = @{$sub_operation};
        return 1
          if ( ( $res eq $sub_op1 || $res eq $sub_op3 ) && $sub_op ne 'OR' );
    }
    return 0;
}

sub is_invalid_xor_or {
    my ( $operations, $res ) = @_;
    foreach my $sub_operation ( values %{$operations} ) {
        my ( $sub_op1, $sub_op, $sub_op3, $sub_res ) = @{$sub_operation};
        return 1
          if ( ( $res eq $sub_op1 || $res eq $sub_op3 ) && $sub_op eq 'OR' );
    }
    return 0;
}

sub find_highest_z_wire {
    my ($wires_ref) = @_;
    my $highest_z = 'z00';

    foreach my $wire ( keys %{$wires_ref} ) {
        if ( $wire =~ /^z/sxm
            && ( substr $wire, 1 ) > ( substr $highest_z, 1 ) )
        {
            $highest_z = $wire;
        }
    }

    return $highest_z;
}

1;

