use strict;
use warnings;
use Readonly;

Readonly my $MODULO => 16_777_216;

sub part1 {
    my @puzzle_input = @_;
    my $result       = 0;

    for my $secret (@puzzle_input) {
        $result += simulate_buyer( $secret, 2000 );
    }

    return $result;
}

sub simulate_buyer {
    my ( $initial_secret, $steps ) = @_;
    my $secret = $initial_secret;
    for ( 1 .. $steps ) {
        $secret = next_secret_number($secret);
    }
    return $secret;
}

sub next_secret_number {
    my ($secret) = @_;
    $secret = ( $secret ^ ( $secret << 6 ) ) % $MODULO;
    $secret = ( $secret ^ ( $secret >> 5 ) ) % $MODULO;
    $secret = ( $secret ^ ( $secret << 11 ) ) % $MODULO;
    return $secret;
}

1;
