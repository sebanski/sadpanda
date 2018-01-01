// Processor object - 
// By: Alex Balzer <zabbal22@gmail.com>
// LICENSE: MIT

import (
	structs.datastore.DataStore
	config.argument_parser.ArgumentParser // TODO: implemtnt this struct and let it do its thing. dont believe.........
	// TODO: implement this.......... plus you need a bunch of imports including.... {os, httpserver, logger, all relative imports to (DataStore, ArgumentParser, ~String)}
	logging
)

var (

)

// TODO: implement this..........
logger := logging.someFuckingTool(__name__)

type Processor struct {
	// TODO: implement this..........
	start_value String
	args ArgumentParser
	key String
	datastore DataStore
}

func (p *Processor) initialize(start_value String, key String, args ArgumentParser) {   // NOTE: dont implement user_inflation in this system.
	// TODO: implement this..........
	p.datastore := p.initialize_blockchain()
	p.args = args
	p.key = key
	p.start_value = start_value
	logger.info("Initialized Processor ....")
}

func (p *Processor) initialize_blockchain() DataStore {
	// TODO: implement this..........
	// initialize you munky.....
	return DataStore{}
}

func (p *Processor) create_ledger(current_value String, key String, args ArgumentParser) Ledger {
	// TODO: implement this..........
	return Ledger{current_value: current_value, key: key, args: args}
}

func (p *Processor) validate(value String) boolean {
	// TODO: implement this..........
  return true
}

func (p *Processor) add_entry(item String) {
	// TODO: implement this..........
	// create Ledger()
	val ledger := Ledger{item: item, encrypted_key: p.get_previous_item(), args: p.args }
	p.datastore.add_item()
  //return {}
}

func (p *Processor) store_ledger(ledger Ledger) {
	// TODO: implement this..........
  p.datastore.add_item(ledger)
}

func (p *Processor) save_datastore(filename String) boolean {
	// TODO: implement this..........
  return True
}

// TODO: fix this bull shit and do a good go lang http server. python wont probably be similar....
func (p *Processor) run_server(args ArgumentParser, server_class HTTPServer, handler_class iHttpServer) {
	// TODO: implement this..........
  
}

func (p *Processor) _run_server(args ArgumentParser) {
	// TODO: basically spawn all the go routinees that will handle http stuff.
	// ADD: the omit block here that will handle the ending of the thread, or whatever it is.
  //return {}
}

func (p *Processor) _initialize(args ArgumentParser) {
	// TODO: implement this..........
}

func (p *Processor) send_key(key String) boolean {
	// TODO: implement
  return true
}

func (p *Processor) delete_key(filename String) {
  // TODO: implemtn
}

func (p *Processor) daemonize(key String, args ArgumentParser) {
  // TODO: implement.... yeah i can spell
}

// func (p *Processor) () {
//   return {}
// }









