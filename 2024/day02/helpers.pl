use List::Util qw(all max);

use strict;
use warnings;

sub is_safe_report {
    my @report = @_;
    my @delta  = map { $report[$_] - $report[ $_ - 1 ] } 1 .. $#report;

    my $all_positive  = all { $_ > 0 } @delta;
    my $all_negative  = all { $_ < 0 } @delta;
    my $max_abs_value = max map { abs } @delta;

    return ( $all_positive || $all_negative ) && $max_abs_value <= 3;
}

1;
