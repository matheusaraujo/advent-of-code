use strict;
use warnings;

use List::Util qw(any);

sub backtrack {
    my ( $idx, $curr, $target, $nums_ref, $op_concat ) = @_;

    if ( $idx > $#{$nums_ref} ) {
        return $curr == $target;
    }
    if ( $curr > $target ) {
        return 0;
    }

    return backtrack( $idx + 1, $curr + $nums_ref->[$idx],
        $target, $nums_ref, $op_concat )
      || (
        backtrack(
            $idx + 1,  $curr * $nums_ref->[$idx], $target,
            $nums_ref, $op_concat
        )
      )
      || (
        $op_concat
        && backtrack(
            $idx + 1,  $curr . $nums_ref->[$idx], $target,
            $nums_ref, $op_concat
        )
      );
}

sub solve {
    my ( $op_concat, $puzzle_input_ref ) = @_;
    my @puzzle_input = @{$puzzle_input_ref};
    my $result       = 0;

    for my $equation (@puzzle_input) {
        my @line   = split /:/sxm, $equation;
        my $target = $line[0];
        my @nums   = split q{ }, $line[1];

        if ( backtrack( 1, $nums[0], $target, \@nums, $op_concat ) ) {
            $result += $target;
        }
    }

    return $result;
}

1;
