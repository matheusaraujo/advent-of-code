use List::Util qw(all max);

use strict;
use warnings;

sub is_safe_report {
    my @line  = @_;
    my @delta = map { $line[$_] - $line[ $_ - 1 ] } 1 .. $#line;

    my $all_positive  = all { $_ > 0 } @delta;
    my $all_negative  = all { $_ < 0 } @delta;
    my $max_abs_value = max map { abs $_ } @delta;

    return ( $all_positive || $all_negative ) && $max_abs_value < 4;
}

1;
