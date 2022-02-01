<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateComputersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('computers', function (Blueprint $table) {
            $table->id();
            $table->integer('user_id')->unsigned()->index();
            $table->string('name');
            $table->string('uuid');
            $table->string('operating_system');
            $table->string('b2_key_id');
            $table->string('b2_application_key');
            $table->timestamp('last_backed_up_at')->nullable();
            $table->unsignedBigInteger('last_backed_up_num_files')->nullable();
            $table->unsignedBigInteger('last_backed_up_size')->nullable();
            $table->softDeletes();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('computers');
    }
}
