include .env

MIGRATION_DIR=migrations

.PHONY: db/migration/new

db/migration/new:
	@if [ -z "$(name)" ]; then \
		echo "Usage: make db/migration/new name=your_migration_name"; \
		exit 1; \
	fi
	@echo "Creating migration file for '${name}' in $(MIGRATION_DIR)"
	migrate create -ext sql -dir $(MIGRATION_DIR) -seq $(name)
## db/migration/up: Apply all 'up' database migrations (default: ./migration)
.PHONY: db/migration/up
db/migration/up: 
	@echo "Running up migrations in $(MIGRATION_DIR)..."
	migrate -path $(MIGRATION_DIR) -database ${BLOG_DSN} up

## db/migration/down: Rollback the last migration
.PHONY: db/migration/down
db/migration/down: 
	@echo "Rolling back last migration in $(MIGRATION_DIR)..."
	migrate -path $(MIGRATION_DIR) -database ${BLOG_DSN} down  

## db/migration/force: Force migrations to a specific version
db/migration/force: 
	@if [ -z "$(version)" ]; then \
		echo "Usage: make db/migration/force version=<target_version>"; \
		exit 1; \
	fi
	@echo "Forcing migration to version $(version) in $(MIGRATION_DIR)..."
	migrate -path $(MIGRATION_DIR) -database $(BLOG_DSN) force $(version)
