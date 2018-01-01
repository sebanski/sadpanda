// Ledger object:   
// By: Alex Balzer <zabbal22@gmail.com>
// LICENSE: MIT

type Ledger struct {
	value String
	key String
	args ArgumentParser
	salt String
}

func (l *Ledger) validate_value() boolean {
	// TODO: implement this feature....
}

func (l *Ledger) initiate_datastore_check() boolean {
	// NOTE: if false is return all hell will break loose. avoid this boolean at all costs. this boolean here is the DEVIL if its `false`.
}
