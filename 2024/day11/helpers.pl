use strict;
use warnings;

sub transform_stone {
    my ($stone) = @_;

    if ( $stone == 0 ) {
        return [1];
    }
    elsif ( length("$stone") % 2 == 0 ) {
        my $mid         = length("$stone") / 2;
        my $left_stone  = substr "$stone", 0, $mid;
        my $right_stone = substr "$stone", $mid;
        return [ $left_stone * 1, $right_stone * 1 ];
    }
    else {
        return [ $stone * 2024 ];
    }
}

1;
