// - DataStore object
// By: Alex Balzer <zabbal22@gmail.com>
// LICENSE: MIT

import (
				UUID
       	config.argument_parser.ArgumentParser // TODO: implemtnt this struct and let it do its thing. dont believe.........
       	// TODO: implement this.......... plus you need a bunch of imports including.... {os, httpserver, logger, all relative imports to (DataStore, ArgumentParser, ~String)}
       	logging
)

var (

)

// TODO: implement this..........
logger := logging.someFuckingTool(__name__)

type DataStore struct {
       	// TODO: implement this..........
       	datastore_id UUID
       	args ArgumentParser
       	datastore []String
}

func (d *DataStore) initialize(args ArgumentParser, datastore []String) {   // NOTE: dont implement user_inflation in this system.
       	// TODO: implement this..........
				d.datastore_id := UUID(random: true)
       	d.datastore := datastore
       	d.args = args
       	logger.info("Initialized DataStore ....")
}

func (d *DataStore) add_item(item String) {
	// TODO: implement this.
}

func (d *DataStore) get_previous_item(item String) {
	// TODO: implement this.
}

func (d *DataStore) check_item(item String) {
	// TODO: implement this.
}


